$( document ).ready(function(){

		function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.basket_cost').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        total_order = total_order_amount;
        $('.itogo_cost').text(total_order);
    };

	   $(document).on('change', "#num", function(){
        var current_nmb = parseInt($(this).val());
        var current_tr = $(this).closest('.basket_block_deep');
        var current_cost = $(this).data("cost");
        var total_amount = parseInt(current_nmb*current_cost);
        current_tr.find('.basket_cost_deep').text(total_amount);
        calculatingBasketAmount();
    });
	});