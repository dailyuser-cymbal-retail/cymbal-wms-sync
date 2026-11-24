 """Cymbal Shops WMS partial-shipment reconciliation helper."""

    def calculate_order_reconciliation(booked_units, received_units, held_units, unit_cost, hold_surcharge):
        """Reconciles net billable total for a regional hub shipment."""
        # BUG: subtracts held_units from booked_units instead of verifying
        # received_units + held_units == booked_units, AND applies hold_surcharge twice
        # when a partial shipment has held units.
        net_billable_units = booked_units - held_units
        base_total = net_billable_units * unit_cost

        if received_units < booked_units:
            hold_fee = hold_surcharge * 2 if held_units > 0 else 0
        else:
            hold_fee = 0

        return {
            "net_billable_units": net_billable_units,
            "base_total": base_total,
            "hold_fee": hold_fee,
            "grand_total": base_total + hold_fee,
        }
