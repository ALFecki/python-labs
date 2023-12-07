import { Routes, Route } from 'react-router-dom';
import Home from './Home/Home';
import Catalog from './Catalog/Catalog';
import About from './About/About';
import FAQ from './FAQ/FAQ';

const AppRouter = () => {
    return (
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/catalog" element={<Catalog />} />
            <Route path="/about" element={<About />} />
            <Route path="/FAQ" element={<FAQ />} />
        </Routes>
    )
}

export default AppRouter;