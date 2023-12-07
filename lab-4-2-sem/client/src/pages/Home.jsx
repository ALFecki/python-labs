import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import '../styles/Navbar.css';

const NavbarItems = () => {
    return (
        <nav className="navbar">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link to="/" className="nav-link">Home</Link>
                </li>
                <li className="nav-item">
                    <Link to="/about" className="nav-link">About</Link>
                </li>
                <li className="nav-item">
                    <Link to="/contact" className="nav-link">Contact</Link>
                </li>
            </ul>
        </nav>
    );
};

const Home = () => {
    return <h1>Welcome to the Home page!</h1>;
};

const About = () => {
    return <h1>About Us</h1>;
};

const Contact = () => {
    return <h1>Contact Us</h1>;
};

const Navbar = () => {
    return (
        <div>
            <NavbarItems />
            <Routes>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
                <Route path="/contact" component={Contact} />
            </Routes>
        </div>
    );
};

export default Navbar;