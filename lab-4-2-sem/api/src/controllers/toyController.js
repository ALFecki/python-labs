const Toy = require('../models/toy');

const toyController = {
    get: async (req, res) => {
        try {
            const filter = {}
            if (req.query.category) {
                filter.category = req.query.category;
            }

            const toys = await Toy.find(filter);
            res.status(200).json(toys);
        } catch (error) {
            console.error(error);
            res.status(500).json({
                name: error.name,
                message: error.message
            });
        }
    },

    getById: async (req, res) => {
        try {
            const toy = await Toy.findById(req.params.id);
            if (!toy) {
                return res.status(404).json({ message: 'Toy not found' });
            }

            res.status(200).json(toy);
        } catch (error) {
            console.error(error);
            res.status(500).json({
                name: error.name,
                message: error.message
            });
        }
    },


    create: async (req, res) => {
        try {
            const newToy = new Toy(req.body);
            await newToy.save();
            res.status(201).json(newToy);
        } catch (error) {
            console.error(error);
            res.status(error.name === 'ValidationError' ? 400 : 500).json({
                name: error.name,
                message: error.message
            });
        }
    },

    update: async (req, res) => {
        try {
            const toy = await Toy.findByIdAndUpdate(
                req.params.id,
                req.body,
                { new: true, runValidators: true }
            );

            if (!toy) {
                return res.status(404).json({ message: 'Toy not found' });
            }

            res.status(200).json(toy);
        } catch (error) {
            console.error(error);
            res.status(error.name === 'ValidationError' ? 400 : 500).json({
                name: error.name,
                message: error.message
            });
        }
    },

    delete: async (req, res) => {
        try {
            const toy = await Toy.findByIdAndDelete(req.params.id);

            if (!toy) {
                return res.status(404).json({ message: 'Toy not found' });
            }

            res.status(200).json({ message: 'Toy deleted successfully' });
        } catch (error) {
            console.error(error);
            res.status(500).json({
                name: error.name,
                message: error.message
            });
        }
    },
};

module.exports = toyController;
