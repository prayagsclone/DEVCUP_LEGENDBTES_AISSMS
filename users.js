const mongoose = require("mongoose");

let userSchema = new mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    email_id: String,
    password: String,
    reg_name: String,
    city: String,
    state: String,
    map_data: String,
    charts_data: String,
    cala_n: [String],
    chart_lab: String,
    slider: array,
    code: String,
    data_location: String

})

module.exports = mongoose.model("users", userSchema);
