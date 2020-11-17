$x = 10; 
sub dynamic_Scoping  
{  
   return $x;  
} 
sub return_D  
{   
   local $x = 20; 
   return dynamic_Scoping();  
} 
print "Dynamic Scoping: ", return_D()."\n"; 
 
$y = 15;
sub static_Scoping
{
    return $y;
}
sub return_S
{
    my $y = 25;
    return static_Scoping();
}
print "Static Scoping: ", return_S()."\n"; 
