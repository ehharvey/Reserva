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
 * 
 * @export
 * @interface RecurringUnavailabilityAllOf
 */
export interface RecurringUnavailabilityAllOf {
    /**
     * the id of an unavailability.
     * @type {string}
     * @memberof RecurringUnavailabilityAllOf
     */
    id: string;
}

/**
 * Check if a given object implements the RecurringUnavailabilityAllOf interface.
 */
export function instanceOfRecurringUnavailabilityAllOf(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "id" in value;

    return isInstance;
}

export function RecurringUnavailabilityAllOfFromJSON(json: any): RecurringUnavailabilityAllOf {
    return RecurringUnavailabilityAllOfFromJSONTyped(json, false);
}

export function RecurringUnavailabilityAllOfFromJSONTyped(json: any, ignoreDiscriminator: boolean): RecurringUnavailabilityAllOf {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
    };
}

export function RecurringUnavailabilityAllOfToJSON(value?: RecurringUnavailabilityAllOf | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
    };
}

