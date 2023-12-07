import { Routes, Route } from 'react-router-dom';
import Home from './Home/Home';
import Catalog from './Catalog/Catalog';
import About from './About/About';
import FAQ from './FAQ/FAQ';
import LoginForm from './Login/Login';
import RegistrationForm from './Register/Register';

const AppRouter = () => {
    return (
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/catalog" element={<Catalog />} />
            <Route path="/about" element={<About />} />
            <Route path="/FAQ" element={<FAQ />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegistrationForm />} />
        </Routes>
    )
}

export default AppRouter;