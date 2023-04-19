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

import {
    NewRecurringUnavailability,
    instanceOfNewRecurringUnavailability,
    NewRecurringUnavailabilityFromJSON,
    NewRecurringUnavailabilityFromJSONTyped,
    NewRecurringUnavailabilityToJSON,
} from './NewRecurringUnavailability';
import {
    NewUnavailability,
    instanceOfNewUnavailability,
    NewUnavailabilityFromJSON,
    NewUnavailabilityFromJSONTyped,
    NewUnavailabilityToJSON,
} from './NewUnavailability';

/**
 * @type UnavailabilitiesPostRequest
 * 
 * @export
 */
export type UnavailabilitiesPostRequest = NewRecurringUnavailability | NewUnavailability;

export function UnavailabilitiesPostRequestFromJSON(json: any): UnavailabilitiesPostRequest {
    return UnavailabilitiesPostRequestFromJSONTyped(json, false);
}

export function UnavailabilitiesPostRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): UnavailabilitiesPostRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return { ...NewRecurringUnavailabilityFromJSONTyped(json, true), ...NewUnavailabilityFromJSONTyped(json, true) };
}

export function UnavailabilitiesPostRequestToJSON(value?: UnavailabilitiesPostRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }

    if (instanceOfNewRecurringUnavailability(value)) {
        return NewRecurringUnavailabilityToJSON(value as NewRecurringUnavailability);
    }
    if (instanceOfNewUnavailability(value)) {
        return NewUnavailabilityToJSON(value as NewUnavailability);
    }

    return {};
}
