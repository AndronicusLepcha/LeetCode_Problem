import java.util.*;
class flowerbed_problem{
    public static void main(String args[]){
        int[] flowerbed={1,0,0,0,1};
        int n=2;
        for(int i=0;i<flowerbed.length;i++){
                if(flowerbed[i]==0 && (i==0 || flowerbed[i-1]==0) && (i== flowerbed.length-1 || flowerbed[i+1]==0)){
                    flowerbed[i]=1;
                    n--;
                    if(n==0){
                        System.out.println("True");
                        System.exit(0);
                    }
                   
                }
        }
        System.out.println("False");
    }
}