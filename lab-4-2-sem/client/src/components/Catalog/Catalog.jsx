import React, { useEffect, useState } from 'react';
import styles from './Catalog.module.css';

const ToyComponent = () => {
    const [categories, setCategories] = useState([]);
    const [toys, setToys] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [suppliers, setSuppliers] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8081/api/category')
            .then(response => response.json())
            .then(data => setCategories(data))
            .catch(error => console.log(error));

        fetch('http://localhost:8081/api/toy')
            .then(response => response.json())
            .then(data => setToys(data))
            .catch(error => console.log(error));

        fetch('http://localhost:8081/api/supplier')
            .then(response => response.json())
            .then(data => setSuppliers(data))
            .catch(error => console.log(error));
    }, []);

    const handleCategoryChange = (event) => {
        const category = event.target.value;
        setSelectedCategory(category);
    };

    const filteredToys = selectedCategory
        ? toys.filter(toy => toy.category === selectedCategory)
        : toys;

    return (
        <div>
            <h2>Категории</h2>
            <select onChange={handleCategoryChange}>
                <option value="">Все категории</option>
                {categories.map(category => (
                    <option key={category._id} value={category._id}>{category.name}</option>
                ))}
            </select>

            <h2>Игрушки</h2>
            <div className={styles.cardContainer}>
                {filteredToys.map(toy => {
                    const supplier = suppliers.find(supplier => supplier.id === toy.supplierid);
                    const category = categories.find(category => category._id === toy.category);
                    return (
                        <div key={toy.id} className={styles.card}>
                            <img src={toy.image} alt={toy.name} />
                            <h3>{toy.name}</h3>
                            <p>{toy.description}</p>
                            <p>Цена: {toy.cost}</p>
                            {category && <p>Категория: {category.name}</p>}
                            {supplier && <p>Поставщик: {supplier.name}</p>}
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default ToyComponent;