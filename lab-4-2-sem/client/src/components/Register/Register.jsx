import React, { useState } from 'react';
import styles from './Register.module.css';

const RegistrationForm = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleFormSubmit = (event) => {
        event.preventDefault();
        // Ваша логика обработки регистрации здесь
    };

    return (
        <div className={styles.registrationForm}>
            <h2>Регистрация</h2>
            <form onSubmit={handleFormSubmit}>
                <div className={styles.formGroup}>
                    <label htmlFor="email">Электронная почта:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={handleEmailChange}
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="username">Логин:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={handleUsernameChange}
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="password">Пароль:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={handlePasswordChange}
                    />
                </div>
                <button type="submit">Зарегистрироваться</button>
            </form>
        </div>
    );
};

export default RegistrationForm;