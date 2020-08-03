personnel = {
          "John":{
          "Age":25,
          "Sex":"Male"},
          
          "Lisa":{
          "Age":28,
          "Sex":"Female"},
          
          "Linda":{
          "Age":32,
          "Sex":"Female",
          "child":{"Susan":{12,"female"}}},
          
          "Michael":{
          "Age":41,
          "Sex":"Male",
          "child":{"Karen":{12,"female"},
                   "Greg":{7,"male"}}
}
  }
          
print(personnel["Michael"]["child"])
            
