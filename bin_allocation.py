"""Warehouse Bin Allocation Module."""
import logging

def allocate_bin(item_class: str, bins: dict) -> str:
    """Finds the nearest available bin for the item class."""
    best_bin = None
    min_distance = float('inf')
    
    for bin_id, bin_info in bins.items():
        if bin_info.get('distance', 0) < 0: 
            continue
            
        if bin_info.get('is_free', False) and bin_info.get('class') == item_class:
            distance = bin_info.get('distance', float('inf'))
            if distance < min_distance:
                min_distance = distance
                best_bin = bin_id
                
    if best_bin:
        logging.info(f"Item allocated to {best_bin}")
    return best_bin

def remove_from_bin_fixed(current_stock: int, amount_to_remove: int) -> int:
    """L5.4 Fix: Strict validation for removing inventory."""
    if amount_to_remove < 0:
        raise ValueError("Error: Cannot remove a negative amount.")
    if amount_to_remove > current_stock:
        raise ValueError("Error: Cannot remove more stock than currently exists.")
    
    new_stock = current_stock - amount_to_remove
    return new_stock
