<template>  
    <div class="container">
        <form>
        
            <div class="form-group">
                <label for="allergies">Allergies</label>
                <input type="text" class="form-control" id="allergies" placeholder="Enter your allergies">
            </div>
            <div class="form-group">
                <label for="fridgeItems">Items in Fridge</label>
                <input type="text" class="form-control" id="fridgeItems" placeholder="Enter items in your fridge">
                
            
                <button type="button" class="btn btn-success" @click="addItem()">Add Item</button>
                <button type="button" class="btn btn-danger" @click="deleteItem()">Delete Item</button>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
                    export default {
                        data() {
                            return {
                                items: []
                            }
                        },
                        methods: {
                            addItem() {
                                let item = document.getElementById('fridgeItems').value;
                                this.items.push(item);
                            },
                            deleteItem() {
                                this.items.pop();
                            }
                        }
                    }
                </script>