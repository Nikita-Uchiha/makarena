

$(document).ready(function(){
calculating();
var total_order_amount = 0;
var total_order = 0;
    function calculatingBasketAmount(){
        total_order_amount = 0;
        
        $('.basket_cost_deep').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        total_order = total_order_amount;
        console.log(total_order_amount);
        $('.page_summ').text(total_order);
        $('#hidan').val(total_order);
    };

    function calculating(){
        var total_order_amount2 = 0;
        
        $('.basket_cost_deep').each(function() {
            total_order_amount2 = total_order_amount2 + parseFloat($(this).text());
        });
        if (total_order_amount2 >= 700 ) {
            
            $('#radio1').attr('data-cost', 0);
            $('#del_cost1').text("0р");
            $('#radio2').attr('data-cost', 100);
            $('#del_cost2').text("100р");
            $('#radio3').attr('data-cost', 200);
            $('#del_cost3').text("200р");
        } else {
             $('#radio1').attr('data-cost', 150);
             $('#del_cost1').text("150р");
            $('#radio2').attr('data-cost', 250);
            $('#del_cost2').text("250р");
            $('#radio3').attr('data-cost', 350);
            $('#del_cost3').text("350р");

        }
        
    };


    $('.radio').click( function() {
    	total_order = 0;
    	
    	var dv = parseFloat($(this).data("cost"));
    	total_order = total_order_amount + dv;
    	console.log(total_order_amount);
    	console.log(dv);
      	$('.page_summ').text(total_order);
        $('#hidan').val(total_order);
    } );
    calculatingBasketAmount();

     $(document).on('change', "#num", function(){
        var current_nmb = parseInt($(this).val());
        var current_tr = $(this).closest('.basket_block_deep');
        var current_cost = $(this).data("cost");
        var total_amount = parseInt(current_nmb*current_cost);
        current_tr.find('.basket_cost_deep').text(total_amount);
        calculating();
        calculatingBasketAmount();
    });


});
