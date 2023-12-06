const Supplier = require('../models/supplier');

const supplierController = {
    getAll: async (req, res) => {
        try {
            const suppliers = await Supplier.find();
            res.status(200).json(suppliers);
        } catch (error) {
            console.error(error);

            const { name, message } = error;
            res.status(500).json({ name, message });
        }
    },

    getById: async (req, res) => {
        try {
            const supplier = await Supplier.findById(req.params.id);
            if (!supplier) {
                return res.status(404).json({ message: 'Supplier not found' });
            }
            res.status(200).json(supplier);
        } catch (error) {
            console.error(error);

            const { name, message } = error;
            res.status(500).json({ name, message });
        }
    },

    create: async (req, res) => {
        try {
            const newSupplier = new Supplier(req.body);
            await newSupplier.save();
            res.status(201).json(newSupplier);
        } catch (error) {
            console.error(error);

            const { name, message } = error;
            res.status(name === 'ValidationError' ? 400 : 500).json({ name, message });
        }
    },

    update: async (req, res) => {
        try {
            const supplier = await Supplier.findByIdAndUpdate(
                req.params.id,
                req.body,
                { new: true, runValidators: true }
            );

            if (!supplier) {
                return res.status(404).json({ message: 'Supplier not found' });
            }

            res.status(200).json(supplier);
        } catch (error) {
            console.error(error);

            const { name, message } = error;
            res.status(name === 'ValidationError' ? 400 : 500).json({ name, message });
        }
    },

    delete: async (req, res) => {
        try {
            const supplier = await Supplier.findByIdAndDelete(req.params.id);

            if (!supplier) {
                return res.status(404).json({ message: 'Supplier not found' });
            }

            res.status(200).json({ message: 'Supplier deleted successfully' });
        } catch (error) {
            console.error(error);

            const { name, message } = error;
            res.status(500).json({ name, message });
        }
    },
};

module.exports = supplierController;