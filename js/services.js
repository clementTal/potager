'use strict';

/* Services */

angular.module('services', ['ngResource'])
    .factory('Service', function ($resource)
    {
        return $resource('api/plante/:key', {},
            {
                list: {method:'GET', params:{key: "list"}, isArray:false},
                add: {method:'POST', params:{key: "add"}, isArray:false},
                delete: {method:'DELETE', params:{key: 'key'}, isArray:false}
            });
    })
;