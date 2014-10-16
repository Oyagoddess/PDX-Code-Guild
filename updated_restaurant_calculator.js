//restaurant calculator created with ryan//
/*create a calculator that will allow users to split or evenly divide their bill and
create individual receipts totals based on menu items ordered.
 */

//added the even_split function we created earlier and added outside of the itemized bill function.
var even_split = function() {
    //created data attributes for each element we need. Adding our previous receipt calculator get check totals.
    var check_total;
    check_total = prompt('What is the total bill?');

    //Parsefloat returns check-total as the actual number not a string.
    check_total = parseFloat(check_total);
     alert('This is the bill before the tip: $' + check_total);

    //create attributes to get diners.
    var total_diners;
    total_diners = prompt('How many diners are there?');
    total_diners = parseInt(total_diners);//ParsInt returns a number

    //create functions and condition to return tip for party less than 6 multiplying check total with .15
    var small_tip = parseFloat(check_total * .15);
        if (total_diners < 6) {
            //toFixed returns a string number with two decimal spaces
            alert("Your party's total tip is: $" + parseFloat(small_tip).toFixed(2));
        }
    //create functions and condition to return tip for party greater than 6 and multiply check total by .18
    var large_party_tip = parseFloat(check_total * .18);
        if (total_diners > 6) {
            alert("Your party's tip is: $" + parseFloat(large_party_tip).toFixed(2));
        }
    //create function calls
    var small_party_total = parseFloat(small_tip + check_total).toFixed(2);

    var large_party_total = parseFloat(large_party_tip + check_total).toFixed(2);

    //create functions and conditions if they choose to split check evenly dependant on party size.
    var even_bill = function(pre_tip_bill, diners) {
        if (diners < 6) {
            alert ('This is the amount each person owes: $' + parseFloat(small_party_total/diners).toFixed(2));
        }

        else {
            alert ('This is the amount each person owes: $' + parseFloat(large_party_total/diners).toFixed(2));
        }
    };
    //function call to run even bill
    even_bill(check_total, total_diners);
};

//create functions for restaurant calculator for individual receipt with their name, specific menu items and totals.
var itemized = function() {

    //set menu
    var menu = {'chicken': 13, 'pizza': 12, 'salad': 7, 'beer': 4, 'wine': 7};

    var party_size = parseInt(prompt("How many people are in your party?"));

    var group = [];// creates a group array

    //create loop that calculates group size starting at 0. counting up to partysize (and continues to ask each person
    //until it reaches partysize.
    for (var i = 0; i < party_size; i++) {
        var individuals = prompt("What's your name?");
        //creates and adds new person as new individual
        var new_individual = new Person(individuals);
        //pushes new individual into the group array.
        group.push(new_individual);
    }
    //create functions to get individual menu items per person.
    var order = function() {

        var ask = function () {

            var follow_up = "y";

            while (follow_up === "y"){
                var order = prompt(group[i].name + ", what did you order?");
                // calls cost per individual in the group
                group[i].getCost(order);

                follow_up = prompt("Did you order anything else?  Answer y for yes or n for no.");
            }
        };
        //function to ask each person in the group for their order.
        for (var i = 0; i < group.length; i++) {
            ask();
        }
    };
    //runs order function
    order();
    //  define "classes" and functions to use to callback in program
    function Person(name) {
        this.name = name;
        this.check = {total: 0, tip: 0, ordered_items: []};

        this.getCost = function (item) {

            this.check.ordered_items.push(item);
            this.check.total += menu[item];
        };

        this.tip = function () {

            var individual_tip = prompt("What percentage do you want to tip?");
            console.log("Your tip amount is " + (individual_tip / 100));
            return this.check.tip = 1 + (individual_tip / 100);

        };

        this.total = function () {
            console.log("Your total bill is " + this.check.total + " with tip " + this.check.tip);
            this.check.total *= this.check.tip;
            return this.check.total * this.check.tip;
        }
    }

    var makeChecks = function () {
        for (var i = 0; i < group.length; i++) {
            alert("ok, " + group[i].name + " your current bill is $" + parseFloat(group[i].check.total).toFixed(2));
            group[i].tip();
            group[i].total();
            alert("your total bill with tip is $" + parseFloat(group[i].check.total).toFixed(2));
        }
    };

    makeChecks();
};

var origin = prompt("Do you want to split the bill evenly or itemize your bill?  To split, enter e, to itemize, enter i.")
    if (origin === "e") {
        even_split();
    }
    else {
        itemized();
    }