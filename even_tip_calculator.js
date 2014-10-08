/**
 * Created by shalonda and ryan  on 10/7/14.
 */

var check_total;
    check_total = prompt('What is the total bill?');
    check_total = parseInt(check_total);
    alert('This is the bill before the tip.' + check_total);

var total_diners;
    total_diners = prompt('How many diners are there?');
    total_diners = parseInt(total_diners);

var small_tip = check_total * .15;
    alert('This is the small tip amount' + small_tip);

var large_party_tip = check_total * .18;
    alert('This is the large party tip amount.' + large_party_tip);

var small_party_total = (small_tip + check_total);

var large_party_total = large_party_tip + check_total;

var even_bill = function(pre_tip_bill, diners) {
    if (diners < 6) {
    alert ('This is the amount for your your group less' + pre_tip_bill / diners);
}
else {
    alert (large_party_total / diners);
}
};
even_bill(check_total, total_diners);




