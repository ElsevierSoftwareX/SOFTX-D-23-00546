import React, { useEffect, useState } from 'react';
import { Navbar } from 'react-bootstrap';
import { useMediaQuery } from 'react-responsive';
import { useLocation } from 'react-router-dom';

function MyNavbar() {
	const [navbarHeight, setNavbarHeight] = useState('90px');
	const [navbarFontSize, setNavbarFontSize] = useState('2.5rem');

	const location = useLocation();
	const isMediumScreen = useMediaQuery({ maxWidth: 991 }); // Set the breakpoint for medium screen (991px)

	useEffect(() => {
		const handleScroll = () => {
			const scrollTop = window.pageYOffset;
			const newNavbarHeight = (90 - Math.min(scrollTop, 50)) + 'px';
			setNavbarHeight(newNavbarHeight);

			const newNavbarFontSize = Math.max((2.5 - (scrollTop * 0.01)), 1.2) + 'rem';
			setNavbarFontSize(newNavbarFontSize);
		};

		window.addEventListener('scroll', handleScroll);

		return () => window.removeEventListener('scroll', handleScroll);
	}, []);

	return (
		<>
			<Navbar className='text-center' expand="lg" fixed="top">
				<Navbar.Brand className='mx-auto' style={{ fontSize: navbarFontSize }} href="">
					KorCAT
				</Navbar.Brand>
			</Navbar>
		</>
	);
}

export default MyNavbar;
