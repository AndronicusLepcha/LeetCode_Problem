class Merge_String_Alternately{
	public static void main(String args[]){
			String s1="andro";
			String s2="lepcha";
			//String s3;
			StringBuilder  s3= new StringBuilder();
			int i=0;
			while(i<s1.length() || i<s2.length()){
				if(i<s1.length()){
					s3.append(s1.charAt(i));
				}
				if(i<s2.length()){
					s3.append(s2.charAt(i));
				}
				i++;
			}
			System.out.println(s3);
	}
}
