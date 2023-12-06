const express = require('express');
const router = express.Router();
const toyController = require('../controllers/toyController');
const authMiddleware = require('../middleware/middleware')

router.get('/', toyController.get);
router.get('/:id', toyController.getById);
router.post('/', authMiddleware, toyController.create);
router.put('/:id', authMiddleware, toyController.update);
router.delete('/:id', authMiddleware, toyController.delete);

module.exports = router;
