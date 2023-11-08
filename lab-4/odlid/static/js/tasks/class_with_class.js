class Toy {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }

    getName() {
        return this.name;
    }

    getPrice() {
        return this.price;
    }
}

class PlushToy extends Toy {
    constructor(name, price, material) {
        super(name, price);
        this.material = material;
    }

    getMaterial() {
        return this.material;
    }
}

function withDiscount(fn, discount) {
    return function () {
        const price = fn.call(this);
        return price - discount;
    }
}

const teddyBear = new PlushToy("Teddy Bear", 20, "Plush");
console.log(teddyBear.getName());
console.log(teddyBear.getPrice());
console.log(teddyBear.getMaterial());

teddyBear.getPrice = withDiscount(teddyBear.getPrice, 5);
console.log(teddyBear.getPrice()); 
