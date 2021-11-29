function pay() {
    if (confirm("Ban chac xoá sinh viên không?") == true)
        fetch("/api/pay", {
            method: 'post'
        }).then(function(res) {
            return res.json()
        }).then(function(data) {
            if (data.error_code == 200){
                location.reload()
                confirm("Thanh toan thanh cong")==true
                window.location.href = "/payed";
                }
            else
                alert("THANH TOAN DANG CO LOI!!! VUI LONG THUC HIEN SAU!")
        })
}