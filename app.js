const express = require("express");
const mongoose = require("mongoose");
const User = require("./users");
const signpg = require("./signpg");
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");
const ejs = require("ejs");
const app = express();

const { response } = require("express");

var jsonParser = bodyParser.json();


app.set('view engine', 'ejs');


// async function main() {
mongoose.connect("mongodb+srv://prayag_SIHH:pp1234@cluster0.tuna9.mongodb.net/tutorial?retryWrites=true&w=majority",
    {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });

// const client = new MongoClient(url);
// try{ await client.connect(); }
// catch(e){ console.log(e); }
// finally{ await client.close(); }
// main();


app.use(bodyParser.urlencoded({ extended: true }));





// const client = new MongoClient(url);
// try{ await client.connect(); }
// catch(e){ console.log(e); }
// finally{ await client.close(); }
// main();


app.post("/", function (req, res) {

    //  res.send("jfffkmek");
    // var s11 = String(req.body.n11);
    // var c11 = String(req.body.n22);
    var r11 = String(req.body.n33);

    // res.send("the sum is"+`<br/><br />email:${s11}<br />password:${c11}<br />`);


    User.find({ "reg_name": r11 }, function (err, users) {

        res.render("dash_home", {

            people: [55, 49, 44, 24, 15],
            // statename: s11,
            // cityname: c11,
            regname: r11,
            usl: users

        });



        // if (err) console.warn(err + "error in user function");
        // console.warn(users);
    });

});


app.post("/chartsjsp", function (req, res) {

    //  res.send("jfffkmek");
    var r11homi = String(req.body.homireg);
    //input box with github link

    User.find({ "reg_name": r11homi }, function (err, users) {

        res.render("charts", {
            regname: r11homi,
            usl: users

        });

    });

});



app.post("/chtohoml", function (req, res) {

    //  res.send("jfffkmek");
    var r11ch = String(req.body.chreg);
    console.log(r11ch);

    // res.send("the sum is"+`<br/><br />email:${s11}<br />password:${c11}<br />`);
    User.find({ "reg_name": r11ch }, function (err, users) {

        res.render("dash_home", {

            people: [55, 49, 44, 24, 15],
            regname: r11ch,
            usl: users

        });



        // if (err) console.warn(err + "error in user function");
        // console.warn(users);
    });


});




app.post("/tables", function (req, res) {

    //  res.send("jfffkmek");
    var r11homit = String(req.body.homiregt);
    //input box with github link

    User.find({ "reg_name": r11homit }, function (err, users) {

        res.render("tables", {
            regname: r11homit,
            usl: users

        });

    });

});


app.post("/tbtohoml", function (req, res) {

    //  res.send("jfffkmek");
    var r11tb = String(req.body.tbreg);
    console.log(r11tb);

    // res.send("the sum is"+`<br/><br />email:${s11}<br />password:${c11}<br />`);
    User.find({ "reg_name": r11tb }, function (err, users) {

        res.render("dash_home", {

            people: [55, 49, 44, 24, 15],
            regname: r11tb,
            usl: users

        });



        // if (err) console.warn(err + "error in user function");
        // console.warn(users);
    });


});



app.post("/chtotable", function (req, res) {

    //  res.send("jfffkmek");
    var r11chhtotb = String(req.body.chtotbreg);
    //input box with github link

    User.find({ "reg_name": r11chhtotb }, function (err, users) {

        res.render("tables", {
            regname: r11chhtotb,
            usl: users

        });

    });

});


app.listen(9000, function (req, res) {
    console.log("9000 port running........ ");
});
