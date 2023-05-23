class Greatest_DivisorofString{
	public static void main(String args[]){
		String s1="ABAB";
		String s2="AB";
		if( !(s1+s2).equals(s2+s1)){
			System.out.println("Null");
		}
		int gcd=1;
		int l1=s1.length();
		int l2=s2.length();
		int min=Math.min(l1,l2);
		for(int i=1;i<=min;i++){
			if(l1 % i == 0 && l2%i==0){
				gcd=i;
			}
		}
		System.out.println(s2.substring(0,gcd));
	}
}
