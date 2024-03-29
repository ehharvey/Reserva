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
/**
 * a group. this could be a project group, a team, or something else. the difference between this and newGroup is that this has an id, which is assigned by the server. it also has timestamps for when the group was created and last updated.
 * @export
 * @interface Group
 */
export interface Group {
    /**
     * the name of the group.
     * @type {string}
     * @memberof Group
     */
    name: string;
    /**
     * the id of a group.
     * @type {string}
     * @memberof Group
     */
    id: string;
    /**
     * the date and time the group was created.
     * @type {Date}
     * @memberof Group
     */
    readonly createDate: Date;
    /**
     * the date and time the group was last updated.
     * @type {Date}
     * @memberof Group
     */
    readonly lastUpdateDate: Date;
    /**
     * id of a user. This is just a string, since the user id is provided by the authentication provider. (in this case, auth0)
     * @type {string}
     * @memberof Group
     */
    owner: string;
}

/**
 * Check if a given object implements the Group interface.
 */
export function instanceOfGroup(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "name" in value;
    isInstance = isInstance && "id" in value;
    isInstance = isInstance && "createDate" in value;
    isInstance = isInstance && "lastUpdateDate" in value;
    isInstance = isInstance && "owner" in value;

    return isInstance;
}

export function GroupFromJSON(json: any): Group {
    return GroupFromJSONTyped(json, false);
}

export function GroupFromJSONTyped(json: any, ignoreDiscriminator: boolean): Group {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
        'id': json['id'],
        'createDate': (new Date(json['createDate'])),
        'lastUpdateDate': (new Date(json['lastUpdateDate'])),
        'owner': json['owner'],
    };
}

export function GroupToJSON(value?: Group | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'id': value.id,
        'owner': value.owner,
    };
}

