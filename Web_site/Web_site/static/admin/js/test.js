numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
var sum = 0;
for(var i=0, length=numbers.length;i<=numbers.length;i++){
    if(numbers[i]%2==0){
        sum+=Math.sqrt(numbers[i]);
    }
    else if(i==numbers.length){
        console.log("Sum is: ",sum);
    }
}
