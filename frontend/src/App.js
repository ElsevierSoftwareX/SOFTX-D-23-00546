import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import { Route, BrowserRouter as Router, Routes, Navigate } from 'react-router-dom';
import './App.css';
import Korcat from './components/Korcat';
import MyNavbar from './components/Navbar';

function App() {
	return (
		<Router>
			<MyNavbar />

			<Routes>
				<Route path="/" element={<Navigate to="/cohesion" />} />
				<Route path="/cohesion" element={<Korcat />} />
				<Route path="/morpheme" element={<Korcat />} />
			</Routes>
		</Router>
	);
}

export default App;
