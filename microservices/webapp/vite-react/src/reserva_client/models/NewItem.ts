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
import type { Feature } from './Feature';
import {
    FeatureFromJSON,
    FeatureFromJSONTyped,
    FeatureToJSON,
} from './Feature';

/**
 * the data required to create a new item. this is the base schema for all item creations. the difference between this and the updateItem schema is that this schema requires all fields to be present.
 * @export
 * @interface NewItem
 */
export interface NewItem {
    /**
     * the name of the item. for now, these will be names of rooms
     * @type {string}
     * @memberof NewItem
     */
    name: string;
    /**
     * the location of the item.
     * @type {string}
     * @memberof NewItem
     */
    location: string;
    /**
     * a description of the item.
     * @type {string}
     * @memberof NewItem
     */
    description: string;
    /**
     * the type of the item. for now, this will only be room.
     * @type {string}
     * @memberof NewItem
     */
    type: NewItemTypeEnum;
    /**
     * the features of the item. for now, these will be the features of the room.
     * @type {Array<Feature>}
     * @memberof NewItem
     */
    features: Array<Feature>;
}


/**
 * @export
 */
export const NewItemTypeEnum = {
    Room: 'room'
} as const;
export type NewItemTypeEnum = typeof NewItemTypeEnum[keyof typeof NewItemTypeEnum];


/**
 * Check if a given object implements the NewItem interface.
 */
export function instanceOfNewItem(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "name" in value;
    isInstance = isInstance && "location" in value;
    isInstance = isInstance && "description" in value;
    isInstance = isInstance && "type" in value;
    isInstance = isInstance && "features" in value;

    return isInstance;
}

export function NewItemFromJSON(json: any): NewItem {
    return NewItemFromJSONTyped(json, false);
}

export function NewItemFromJSONTyped(json: any, ignoreDiscriminator: boolean): NewItem {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
        'location': json['location'],
        'description': json['description'],
        'type': json['type'],
        'features': ((json['features'] as Array<any>).map(FeatureFromJSON)),
    };
}

export function NewItemToJSON(value?: NewItem | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'location': value.location,
        'description': value.description,
        'type': value.type,
        'features': ((value.features as Array<any>).map(FeatureToJSON)),
    };
}

