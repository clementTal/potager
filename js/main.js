function MainCtrl($scope, Service)
{
    $scope.potagers = [];
    $scope.addPotager = function()
    {
        $scope.message = "";
        Service.add(function(result)
        {
            $scope.message = "un potager a bien été ajouté";
            $scope.getAllPotager();
        });
    };

    $scope.getAllPotager = function()
    {
        Service.list(function(result)
        {
            $scope.potagers = result.potager;
            Angular.forEach($scope.potagers, function(potager) {
                potager.showMore = false;
            })

        });
    };

    $scope.deletePotager = function(key)
    {
        Service.delete({key: key}, function(result)
        {
           $scope.message = "un potager a bien été supprimé";
           $scope.getAllPotager();
        });
    };
}