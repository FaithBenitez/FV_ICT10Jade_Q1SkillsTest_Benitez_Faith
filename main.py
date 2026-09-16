from pyscript import document, display

def create_order(e):
    document.getElementById("output2").innerHTML = " "  # clears previous result

    # Get each item element
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
 

    pastry = document.getElementById("Pastry")
    pastry_price = float(pastry.value)

    # Calculate subtotal 
    subtotal = (float(prod1.value) * prod1.checked
                + float(prod2.value) * prod2.checked
                + float(prod3.value) * prod3.checked
                + float(prod4.value) * prod4.checked
                + float(prod5.value) * prod5.checked)       

    
    size = document.querySelector("input[name='size']:checked")
    size_price = float(size.value)

    # Tax and price with tax
    tax_rate = 0.12  
    tax = subtotal * tax_rate
    
    # Grand total
    total = subtotal + size_price + tax + pastry_price

    display(f"Total: P{total}.", target="output1")
    display(f"Subtotal: P{subtotal}.", target="output1")
    display(f"Tax: P{tax}.", target="output1", append=True)
    display(f"Thank you for your order!", target="output1", append=True)
