'use strict';

/* Services */

angular.module('services', ['ngResource'])
    .factory('Service', function ($resource)
    {
        return $resource('service/:key', {},
            {
                list: {method:'GET', params:{}, isArray:false},
                add: {method:'PUT', params:{}, isArray:false},
                delete: {method:'DELETE', params:{key: 'key'}, isArray:false}
            });
    })
;