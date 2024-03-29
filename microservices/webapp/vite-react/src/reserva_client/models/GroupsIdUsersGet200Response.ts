/* tslint:disable */
/* eslint-disable */
/**
 * Main API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { User } from './User';
import {
    UserFromJSON,
    UserFromJSONTyped,
    UserToJSON,
} from './User';

/**
 * 
 * @export
 * @interface GroupsIdUsersGet200Response
 */
export interface GroupsIdUsersGet200Response {
    /**
     * 
     * @type {Array<User>}
     * @memberof GroupsIdUsersGet200Response
     */
    users?: Array<User>;
}

/**
 * Check if a given object implements the GroupsIdUsersGet200Response interface.
 */
export function instanceOfGroupsIdUsersGet200Response(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function GroupsIdUsersGet200ResponseFromJSON(json: any): GroupsIdUsersGet200Response {
    return GroupsIdUsersGet200ResponseFromJSONTyped(json, false);
}

export function GroupsIdUsersGet200ResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): GroupsIdUsersGet200Response {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'users': !exists(json, 'users') ? undefined : ((json['users'] as Array<any>).map(UserFromJSON)),
    };
}

export function GroupsIdUsersGet200ResponseToJSON(value?: GroupsIdUsersGet200Response | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'users': value.users === undefined ? undefined : ((value.users as Array<any>).map(UserToJSON)),
    };
}

