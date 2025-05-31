# EDA Visual Summary
## Summary of Visuals
- Share of Late Deliveries: Majority of orders are on time.
- Review Score Distribution: Most customers leave 5-star reviews.
- Delay vs Review: Late deliveries lead to more negative reviews.

## What are problematic orders?

Orders with:
- Late delivery (`is_late == 1`) OR
- Poor review score (≤ 2)

## Summary of the model

- **Features used**: `wait_time`, `price`, `freight_value`

**Business Implications:**

Our predictive model allows Trendify to identify potentially problematic orders *before* they occur. 
This means:

-  Operations teams can prioritize high-risk orders for proactive intervention (e.g., faster fulfillment or improved communication).
-  Customer service can better anticipate complaints and prepare solutions.
-  Sellers with consistently flagged orders can be evaluated and supported for better service (can be monitored).

With this intelligence, Trendify can boost customer satisfaction and retention, while reducing complaint-related costs.

*Note: The model achieves ~87% accuracy with strong performance in identifying non-problematic orders. Performance on problematic orders (precision: 70%, recall: 48%) gives a good starting point for risk flagging.*


