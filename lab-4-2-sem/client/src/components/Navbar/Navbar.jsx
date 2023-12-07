import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Navbar.module.css'

const Navbar = () => {
    return (
        <nav className={styles.navbar}>
            <ul>
                <li>
                    <Link to="/">Главная</Link>
                </li>
                <li>
                    <Link to="/catalog">Каталог</Link>
                </li>
                <li>
                    <Link to="/about">О нас</Link>
                </li>
                <li>
                    <Link to="/FAQ">FAQ</Link>
                </li>
                <li>
                    <Link to="/register">Регистрация</Link>
                </li>
                <li>
                    <Link to="/login">Вход</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;