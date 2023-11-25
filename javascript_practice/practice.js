let fruits_dic = {"apples":500, "bananas":200}
fruits_dic["grapes"] = 100
for (const [key, value] of Object.entries(fruits_dic)){
    console.log(key, value, '--------')
}
console.log(fruits_dic)