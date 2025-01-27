create function get_total_order_cost(@order_id int)
    returns int
    as
    begin
        declare @total_cost float
        select @total_cost = sum(price) from Order_details where order_id = @order_id
        return @total_cost
    end
go

