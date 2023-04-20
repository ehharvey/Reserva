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
import type { GroupMembership } from './GroupMembership';
import {
    GroupMembershipFromJSON,
    GroupMembershipFromJSONTyped,
    GroupMembershipToJSON,
} from './GroupMembership';

/**
 * 
 * @export
 * @interface UsersMeGroupsGet200Response
 */
export interface UsersMeGroupsGet200Response {
    /**
     * 
     * @type {Array<GroupMembership>}
     * @memberof UsersMeGroupsGet200Response
     */
    groups?: Array<GroupMembership>;
}

/**
 * Check if a given object implements the UsersMeGroupsGet200Response interface.
 */
export function instanceOfUsersMeGroupsGet200Response(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function UsersMeGroupsGet200ResponseFromJSON(json: any): UsersMeGroupsGet200Response {
    return UsersMeGroupsGet200ResponseFromJSONTyped(json, false);
}

export function UsersMeGroupsGet200ResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): UsersMeGroupsGet200Response {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'groups': !exists(json, 'groups') ? undefined : ((json['groups'] as Array<any>).map(GroupMembershipFromJSON)),
    };
}

export function UsersMeGroupsGet200ResponseToJSON(value?: UsersMeGroupsGet200Response | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'groups': value.groups === undefined ? undefined : ((value.groups as Array<any>).map(GroupMembershipToJSON)),
    };
}

