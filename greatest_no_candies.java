class greatest_no_candies{
    public static void main(String args[]){
        int arr[]={2,4,5,1};
        int extra=2;
        Boolean[] re=new Boolean[4];
        for(int i=0;i<arr.length;i++){
            if( arr[i]+extra > 5){
                re[i]=true;
            }
            else{
                re[i]=false;
            }
        }
        for(int i=0;i<4;i++){
            System.out.println(re[i]);
        }
    }
}