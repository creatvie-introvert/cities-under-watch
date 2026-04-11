const stripePublicKey = JSON.parse(
    document.getElementById('id_stripe_public_key').textContent
);
const clientSecret = JSON.parse(
    document.getElementById('id_client_secret').textContent
);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const style = {
    base: {
        color: "#f5f5f5",
        fontFamily: "Roboto, Arial, sans-serif",
        fontSmoothing: "antialised",
        fontSize: "16px",
        "::placeholder": {
            color: "#8c919b",
        },
    },
    invalid: {
        color: "#ff9f9f",
        iconColor: "#ff9f9f",
    },
};

const card = elements.create("card", { style: style });
card.mount("#card-element");

const cardElementContainer = document.getElementById("card-element");

card.on("focus", function () {
    cardElementContainer.classList.add("checkout-form__card-element--focus");
});

card.on("blur", function() {
    cardElementContainer.classList.remove("checkout-form__card-element--focus");
});

card.addEventListener("change", function(event) {
    const errorDiv = document.getElementById("card-errors");

    if (event.error) {
        errorDiv.textContent = event.error.message;
        cardElementContainer.classList.add("checkout-form__card-element--invalid");
    } else {
        errorDiv.textContent = "";
        cardElementContainer.classList.remove("checkout-form__card-element--invalid");
    }
});