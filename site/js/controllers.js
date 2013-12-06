var waasApp = angular.module('waasApp', []);

waasApp.controller('WallpaperSplashController', function($scope, $timeout) {
    $scope.wallpapers = [{
        'source': 'site/images/wallpaper1.jpg'
    }, {
        'source': 'site/images/wallpaper2.jpg'
    }, {
        'source': 'site/images/wallpaper3.jpg'
    }];

    $scope.getStyle = function(wallpaper) {
        var dist = 20 * $scope.wallpapers.indexOf(wallpaper);
        return "top: " + dist + "px; left: " + dist + "px;";
    };

    $scope.features = [{
        text: "Accounts, that let you have consistent wallpapers across multuiple machines"
    }, {
        text: "Wallpapers playlists"
    }, {
        text: "Wallpaper browsing and discovery"
    }, {
        text: "Potentially users can \"sell\" wallpapers they've created"
    }];

    function cycle() {
        $timeout(function() {
            $scope.wallpapers.unshift($scope.wallpapers.pop());
            console.log("Heyo");
            cycle();
        }, 5000);
    }
    cycle();
});