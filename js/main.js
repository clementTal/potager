function MainCtrl($scope, Service)
{
    $scope.potagers = [];
    $scope.addPotager = function()
    {
        $scope.message = "";
        var plante = {
            nom: "carotte",
            FamillePlante: "carotte",
            SoleilPlante: "soleil",
            TypePlante: "carotte",
            cycleCulture: "cycleCulture",
            hauteurPlante: 1,
            nbCarreRequis: 2,
            quantiteCarre: 1,
            recolte: [1, 2],
            semisTerre: [1, 2],
            semisTerreProtection:[1, 2],
            sol: "sol",
            tempsOccupationCarre: 0,
            tempsRotationCarre: 0,
            variete:"racine"
        }
        Service.add(plante, function(result)
        {
            $scope.message = "une plante a bien été ajouté";
            $scope.getAllPotager();
        });
    };

    $scope.getAllPotager = function()
    {
        Service.list(function(result)
        {
            $scope.plantes = result.plantes;
            Angular.forEach($scope.plantes, function(potager) {
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