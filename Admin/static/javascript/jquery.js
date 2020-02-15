$(document).ready(()=>{
		$("#employeesearch").click(()=>{
		$.ajax({
			data:{search:$("#employeesearch").val()},
				url:'/employeesearch',
				method:'GET',
				success:function(data){
				console.log(data)
					$("tr").not("tr:first").remove();
					let html="";
		
					for(employee of data){
	
						html+="<tr>";
							html+="<td>"+employee.employee_id+"</td>";
							html+="<td>"+employee.first_name+"</td>";
							html+="<td>"+employee.last_name+"</td>";
							html+="<td>"+employee.address+"</td>";
							html+="<td>"+employee.contact+"</td>";
							html+="<td>"+employee.Email+"</td>";
							html+="<td>"+employee.position+"</td>";
							html+="<td><a href='/edit/"+employee.employee_id+"'>Edit</a> &nbsp;| <a href='/delete/"+employee.employee_id+"'>Delete</a></td>";
							html+="</tr>";
					$("table").append(html);
						}

					},error:function(error){
				console.log(error)
				},complete:function(){
				console.log("complete")
			}
			})
		})
		$(document).ready(()=>{
		$("#Customersearch").click(()=>{
		$.ajax({
			data:{search:$("#Customersearch").val()},
				url:'/Customersearch',
				method:'GET',
				success:function(data){
				console.log(data)
					$("tr").not("tr:first").remove();
					let html="";
					for(customer of data){
	
						html+="<tr>";
							html+="<td>"+customer.Customer_id+"</td>";
							html+="<td>"+customer.first_name+"</td>";
							html+="<td>"+customer.last_name+"</td>";
							html+="<td>"+customer.address+"</td>";
							html+="<td>"+customer.email+"</td>";
							html+="<td>"+customer.service+"</td>";
							html+="</tr>";
					$("table").append(html);
						}

					},error:function(error){
				console.log(error)
				},complete:function(){
				console.log("complete")
			}
			})
		})
	})

})