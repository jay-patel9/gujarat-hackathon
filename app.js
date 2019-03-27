const express = require("express"),
    bodyParser = require("body-parser"),
    mongoose = require("mongoose");


mongoose.connect("mongodb://localhost/hackathon", { useNewUrlParser: true });
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

var userSchema = mongoose.Schema({
    license_id: String,
    used: {
        type: Date,
        default: Date.now
    },
    fingerprint_id: String,
    suspended: Number,
});




app.get("/data", function (req, res) {
    res.send("get");
});


app.post("/data", function (req, res) {
    var license_id = req.body.license_id;
    var license = license_id;
    var fingerprint_id = req.body.fingerprint_id;
    var suspended = req.body.suspended;
    var data = { license_id: license_id, fingerprint_id: fingerprint_id, suspended: suspended }
    if(Number(suspended) != 1){
        const license1 = mongoose.model(license, userSchema);
        license1.create(data, function (err, data) {
            if (err) {
                console.log(err);
            }
            console.log(data);
        });
    }
    else{
        console.log("you cannot drive");
    }
});

app.listen(3000, function (err) {
    console.log("started");
})