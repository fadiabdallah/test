<html>
<body>

<?php

	// set your infomation.
	$host		=	'localhost';
	$user		=	'root';
	$pass		=	'';	
	$database	=	'telephone';
	
	
	// connect to the mysql database server.
	$connect = @mysql_connect ( $host, $user, $pass ) ;
    $name= $_POST['contact_name'];
    $mobile= $_POST['contact_mobile_number'];

	if ( $connect )
	{
		mysql_select_db ( $database, $connect );
        $query = "DELETE FROM contacts WHERE contact_mobile='" . $mobile . "'";

		// $query="DELETE FROM contacts WHERE contact_name={$name} " ;

		
		if ( @mysql_query ( $query ) )
			{
				echo 'Record Deleted Successfuly';  
			}
			else {
				die ( mysql_error() );
			}	
	        
	}
	else {
		trigger_error ( mysql_error(), E_USER_ERROR );
	}

	

        
			
?>


</body>
</html>