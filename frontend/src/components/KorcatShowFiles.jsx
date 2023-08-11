import React, { useEffect, useState } from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Badge from 'react-bootstrap/Badge';
import { useLocation } from 'react-router-dom';
import Tab from 'react-bootstrap/Tab';
import Table from 'react-bootstrap/Table';
import Tabs from 'react-bootstrap/Tabs';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';


function KorcatShowFiles() {
	const location = useLocation();
	const currentPath = location.pathname;
	const tab = currentPath.split('/').pop();

	const [cfiles, setCfiles] = useState([]);
	const [mfiles, setMfiles] = useState([]);
	const [error, setError] = useState(null);
	const [selectedTraits, setSelectedTraits] = useState([]);

	useEffect(() => {
		async function fetchFiles() {
			try {
				const response = await fetch('http://165.246.44.247:3000/file/korcat');
				if (!response.ok) {
					throw new Error(`HTTP error! status: ${response.status}`);
				}
				const cfiles = await response.json();
				setCfiles(cfiles);
			} catch (error) {
				setError(error);
			}

			try {
				const response = await fetch('http://165.246.44.247:3000/file/morpheme');
				if (!response.ok) {
					throw new Error(`HTTP error! status: ${response.status}`);
				}
				const mfiles = await response.json();
				setMfiles(mfiles);
			} catch (error) {
				setError(error);
			}
		}
		fetchFiles();
	}, []);

	if (error) {
		return <div>Error: {error.message}</div>;
	}

	const handleCheckboxChange = (event, fileId, resultKey, value) => {
		if (event.target.checked) {
			setSelectedTraits((prevSelectedTraits) => [
				...prevSelectedTraits,
				{ fileId, resultKey, value },
			]);
		} else {
			setSelectedTraits((prevSelectedTraits) =>
				prevSelectedTraits.filter(
					(item) => !(item.fileId === fileId && item.resultKey === resultKey)
				)
			);
		}
	};

	const handleFileSelectAll = (fileId) => {
		const fileSelected = selectedTraits.some((item) => item.fileId === fileId);
		if (fileSelected) {
			setSelectedTraits((prevSelectedTraits) =>
				prevSelectedTraits.filter((item) => item.fileId !== fileId)
			);
		} else {
			const resultKeys = cfiles.find((file) => file._id === fileId)?.results;
			if (resultKeys) {
				const fileSelectedTraits = Object.keys(resultKeys).map((resultKey) => ({
					fileId,
					resultKey,
					value: resultKeys[resultKey],
				}));
				setSelectedTraits((prevSelectedTraits) => [
					...prevSelectedTraits,
					...fileSelectedTraits,
				]);
			}
		}
	};

	const convertToCSV = () => {
		const csvContent = selectedTraits
			.map((trait) => `${trait.resultKey},${trait.value}`)
			.join('\n');
		const csvData = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
		const link = document.createElement('a');
		link.href = URL.createObjectURL(csvData);
		link.setAttribute('download', 'selected_traits.csv');
		link.click();
	};

	return (
		<>
			<Tabs defaultActiveKey={tab} fill>
				<Tab eventKey="cohesion" title="Cohesion">
					{cfiles.length > 0 ? (
						<Accordion defaultActiveKey={cfiles.length > 0 ? cfiles[cfiles.length - 1]._id : null} className="my-accordion" flush>
							{cfiles.map((file) => (
								<Accordion.Item eventKey={file._id} key={file._id}>
									<Accordion.Header>
										<Badge pill bg="dark" text="light">
											{file._id.slice(0, -14)}
										</Badge>
										&nbsp;&nbsp;
										{file.filename}
									</Accordion.Header>
									<Accordion.Body>
										<div className='row row-cols-1 row-cols-md-2'>
											<div className='col file-contents'>
												{file.contents}
												<hr />
											</div>

											<div className='col'>
												<div>
													<input
														type="checkbox"
														class="btn-check" id={file._id} autocomplete="off"
														checked={selectedTraits.some(
															(item) => item.fileId === file._id
														)}
														onChange={() => handleFileSelectAll(file._id)}
													/>
													<label class="btn btn-secondary btn-sm" for={file._id}>Select All</label>

													&nbsp;

													<button type="button" className="btn btn-secondary btn-sm" onClick={convertToCSV}>Download as .CSV</button>
												</div>

												<br />

												<div className='results-table'>
													<Table hover size="sm" className='table-container'>
														{file.results && typeof file.results === 'object' ? (
															<tbody>
																{Object.entries(file.results).map(
																	([key, value], index) => (
																		<tr key={index}>
																			<td className="check-td">
																				<input
																					type="checkbox"
																					checked={selectedTraits.some(
																						(item) =>
																							item.fileId === file._id &&
																							item.resultKey === key
																					)}
																					onChange={(e) =>
																						handleCheckboxChange(
																							e,
																							file._id,
																							key,
																							value
																						)
																					}
																				/>
																			</td>
																			<td className='type-td'>
																				{key}
																			</td>
																			<td className='value-td'>
																				{Number.isInteger(value) ? value.toFixed(0) : value.toFixed(5)}
																			</td>
																		</tr>
																	)
																)}
															</tbody>
														) : (
															<p>No results found.</p>
														)}
													</Table>
												</div>
											</div>
										</div>
									</Accordion.Body>
								</Accordion.Item>
							)).reverse()}
						</Accordion>
					) : (
						<p class="card-text placeholder-glow" style={{ padding: "20px" }}>
							<span class="placeholder col-7"></span>
							<span class="placeholder col-4"></span>
							<span class="placeholder col-4"></span>
							<span class="placeholder col-6"></span>
							<span class="placeholder col-8"></span>
						</p>
					)}
				</Tab>
				<Tab eventKey="morpheme" title="Morpheme">
					{mfiles.length > 0 ? (
						<Accordion defaultActiveKey={mfiles.length > 0 ? mfiles[mfiles.length - 1]._id : null} className="my-accordion" flush>
							{mfiles.map((file) => (
								<Accordion.Item eventKey={file._id} key={file._id}>
									<Accordion.Header>
										<Badge pill bg="dark" text="light">
											{file._id.slice(0, -14)}
										</Badge>
										&nbsp;&nbsp;
										{file.filename}
									</Accordion.Header>
									<Accordion.Body>
										<div className='row row-cols-1 row-cols-md-2'>
											<div className='col file-contents'>
												{file.contents}
												<hr />
											</div>

											<div className='col'>
												<div className='results-table'>
													{file.results}
												</div>
											</div>
										</div>
									</Accordion.Body>
								</Accordion.Item>
							)).reverse()}
						</Accordion>
					) : (
						<p class="card-text placeholder-glow" style={{ padding: "20px" }}>
							<span class="placeholder col-7"></span>
							<span class="placeholder col-4"></span>
							<span class="placeholder col-4"></span>
							<span class="placeholder col-6"></span>
							<span class="placeholder col-8"></span>
						</p>
					)}
				</Tab>
			</Tabs>
		</>
	);
}

export default KorcatShowFiles;
