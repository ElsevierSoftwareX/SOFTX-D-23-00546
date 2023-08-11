import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import Accordion from 'react-bootstrap/Accordion';
import { useAccordionButton } from 'react-bootstrap/AccordionButton';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Spinner from 'react-bootstrap/Spinner';
import FloatingLabel from 'react-bootstrap/esm/FloatingLabel';
import '../App.css';


function CustomToggle({ children, eventKey, selectedFiles }) {
	const decoratedOnClick = useAccordionButton(eventKey, () =>
		console.log('totally custom!')
	);

	const handleClick = (event) => {
		event.preventDefault();
		event.stopPropagation();
		decoratedOnClick();
	};

	const isButtonDisabled = !selectedFiles || selectedFiles.length === 0;

	return (
		<Button
			disabled={isButtonDisabled}
			className="rounded-end-pill"
			variant="dark"
			id="button-addon2"
			onClick={handleClick}
			style={{ color: "white", margin: 'none' }}
		>
			{children}
		</Button>
	);
}


function KorcatAddFile() {
	const [selectedFiles, setSelectedFiles] = useState([]);
	const [uploadInProgress, setUploadInProgress] = useState(false);
	const [selectedFilesContent, setSelectedFilesContent] = useState([]);
	const [editedFlags, setEditedFlags] = useState([]);
	const [analysisType, setAnalysisType] = useState('cohesion'); // Default choice

	const handleFileSelect = async (event) => {
		const newSelectedFiles = Array.from(event.target.files);
		const newSelectedFilesContent = await Promise.all(newSelectedFiles.map(async (file) => await file.text()));

		setSelectedFiles(newSelectedFiles);
		setSelectedFilesContent(newSelectedFilesContent);
		setEditedFlags(newSelectedFiles.map(() => false)); // Initialize with false values
	};

	const handleAnalysisTypeChange = (event) => {
		setAnalysisType(event.target.value);
	};

	const handleUpload = async (event) => {
		event.preventDefault();
		setUploadInProgress(true);

		const formData = new FormData();

		selectedFiles.forEach((file, index) => {
			const content = editedFlags[index] ? selectedFilesContent[index] : file;
			formData.append("files", new Blob([content], { type: "text/plain" }), file.name);
		});

		const url = analysisType === 'cohesion' ? 'http://165.246.44.247:3000/file/korcat' : 'http://165.246.44.247:3000/file/morpheme';

		try {
			const response = await fetch(url, {
				method: 'POST',
				body: formData,
			});

			const data = await response.json();
			console.log(data);

			setSelectedFiles([]);
			setSelectedFilesContent([]);
			setEditedFlags([]);
		} catch (error) {
			console.error(error);
		} finally {
			setUploadInProgress(false);

			if (analysisType === 'cohesion') {
				window.location.href = '/cohesion';
			} else if (analysisType === 'morpheme') {
				window.location.href = '/morpheme';
			}
		}
	};

	return (
		<div>
			<form onSubmit={handleUpload}>
				<Accordion defaultActiveKey="0">
					<Card id="file-contents-accordion">
						<Card.Header>
							<InputGroup className="inputgroup">
								<Form.Control
									className="rounded-start-pill border-dark"
									type="file"
									id="fileInput"
									aria-describedby="basic-addon2"
									multiple
									accept=".txt"
									onChange={handleFileSelect}
								/>
								<CustomToggle eventKey="1" selectedFiles={selectedFiles}>
									&nbsp;<i class="bi bi-pencil-square"></i>&nbsp;Edit File&nbsp;
								</CustomToggle>
							</InputGroup>
						</Card.Header>
						{selectedFiles.length > 0 && (
							<Accordion.Collapse eventKey='1'>
								<Card.Body>
									{selectedFiles.map((file, index) => (
										<div className="mt-3" key={index}>
											<FloatingLabel
												controlId="floatingTextarea"
												label={"File " + (index + 1)}
												className="mb-3"
											>
												<Form.Control
													as="textarea"
													style={{ height: "200px" }}
													placeholder="Leave a comment here"
													className="form-control rounded"
													value={selectedFilesContent[index]}
													onChange={(event) => {
														const newContent = event.target.value;
														setSelectedFilesContent((prevContent) => {
															const updatedContent = [...prevContent];
															updatedContent[index] = newContent;
															return updatedContent;
														});
													}}
												/>
											</FloatingLabel>
											<Button
												className="btn btn-secondary"
												onClick={() => {
													setSelectedFilesContent((prevContent) => {
														const updatedContent = [...prevContent];
														updatedContent[index] = selectedFilesContent[index];
														return updatedContent;
													});
													setEditedFlags((prevFlags) => {
														const updatedFlags = [...prevFlags];
														updatedFlags[index] = true;
														return updatedFlags;
													});
												}}
											>
												Confirm Edit
											</Button>
										</div>
									))}
								</Card.Body>
							</Accordion.Collapse>
						)}
					</Card>
				</Accordion>

				<div class="container text-center" style={{ paddingTop: "2rem" }}>
					<div class="row align-items-center justify-content-center">
						<div className="col-auto row">
							<Form.Check
								className='col'
								type="radio"
								label="Cohesion"
								name="analysisType"
								value="cohesion"
								checked={analysisType === 'cohesion'}
								onChange={handleAnalysisTypeChange}
							/>
							<Form.Check
								className='col'
								type="radio"
								label="Morpheme"
								name="analysisType"
								value="morpheme"
								checked={analysisType === 'morpheme'}
								onChange={handleAnalysisTypeChange}
							/>
						</div>

						<Button
							className="rounded-pill btn-secondary col-auto"
							variant="dark"
							type="submit"
							disabled={uploadInProgress || selectedFiles.length === 0}
						>
							{uploadInProgress ? (
								<>
									Analyzing
									<Spinner
										className="ms-2"
										animation="border"
										role="status"
										size="sm"
									/>
								</>
							) : (
								"Analyze"
							)}
						</Button>
					</div>
				</div>
			</form>
		</div>
	);
}

export default KorcatAddFile;
