class reverse_words{
    public static void main(String args[]){
        String s=" hello, robot is online ";
        int i,n;
        StringBuilder sb= new StringBuilder();

        String[] words=s.split(" ");
        
        //for(i=0;i<words.length;i++){
          //  System.out.print(words[i]+ " ");
        //}
        for(i=words.length-1;i>=0;i--){
            if(words[i] != ""){ //to remove first space
                sb.append(words[i]);
                sb.append(" ");
            }
        }
        sb.setLength(sb.length()-1); //delete last space
        System.out.println(sb);
    }
}