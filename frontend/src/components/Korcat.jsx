import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

import React from 'react';

import KorcatAddFile from './KorcatAddFile';
import KorcatShowFiles from './KorcatShowFiles';


function Korcat() {
	return (
		<Container fluid>
			<div style={{ marginTop: "6em" }}>
				<Row className="justify-content-center" style={{ paddingTop: "8em" }}>
					<Col xs={12} md={6} className="addfile">
						<h5 className='text-center headings'>Upload File</h5>
						<KorcatAddFile />
					</Col>
				</Row>

				<Row className="justify-content-center" style={{ paddingTop: "5em" }}>
					<Col className='showfiles'>
						<h5 className='text-center headings'>Analysis Results</h5>
						<Card border="dark">
							<Card.Body>
								<KorcatShowFiles />
							</Card.Body>
						</Card>
					</Col>
				</Row>
			</div>
		</Container>
	);
}

export default Korcat;