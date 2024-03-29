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
 * a new unavailability. this is sent when a client wants to create a new unavailability.
 * @export
 * @interface NewUnavailability
 */
export interface NewUnavailability {
    /**
     * the id of the item. 
     * @type {string}
     * @memberof NewUnavailability
     */
    item: string;
    /**
     * date-time string with 15-minute interval, e.g., 2023-04-02t12:00:00
     * @type {string}
     * @memberof NewUnavailability
     */
    startDate: string;
    /**
     * date-time string with 15-minute interval, e.g., 2023-04-02t12:00:00
     * @type {string}
     * @memberof NewUnavailability
     */
    endDate: string;
    /**
     * the id of the owner of the unavailability.
     * It can be a group or a user
     * @type {string}
     * @memberof NewUnavailability
     */
    owner?: string;
    /**
     * 
     * @type {string}
     * @memberof NewUnavailability
     */
    type: NewUnavailabilityTypeEnum;
}


/**
 * @export
 */
export const NewUnavailabilityTypeEnum = {
    Maintenance: 'maintenance',
    Booking: 'booking',
    OffHours: 'offHours',
    Other: 'other'
} as const;
export type NewUnavailabilityTypeEnum = typeof NewUnavailabilityTypeEnum[keyof typeof NewUnavailabilityTypeEnum];


/**
 * Check if a given object implements the NewUnavailability interface.
 */
export function instanceOfNewUnavailability(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "item" in value;
    isInstance = isInstance && "startDate" in value;
    isInstance = isInstance && "endDate" in value;
    isInstance = isInstance && "type" in value;

    return isInstance;
}

export function NewUnavailabilityFromJSON(json: any): NewUnavailability {
    return NewUnavailabilityFromJSONTyped(json, false);
}

export function NewUnavailabilityFromJSONTyped(json: any, ignoreDiscriminator: boolean): NewUnavailability {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'item': json['item'],
        'startDate': json['startDate'],
        'endDate': json['endDate'],
        'owner': !exists(json, 'owner') ? undefined : json['owner'],
        'type': json['type'],
    };
}

export function NewUnavailabilityToJSON(value?: NewUnavailability | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'item': value.item,
        'startDate': value.startDate,
        'endDate': value.endDate,
        'owner': value.owner,
        'type': value.type,
    };
}

