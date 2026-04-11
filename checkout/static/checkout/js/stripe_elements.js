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
        fontSmoothin: "antialised",
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

card.addEventListener("change", function(event) {
    const errorDiv = document.getElementById("card-errors");

    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = "";
    }
});