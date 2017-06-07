package com.squarepegsystems.boot2.repo;

import com.squarepegsystems.boot2.entity.StormType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

/**
 * Created by mikeh on 6/6/17.
 */
@RepositoryRestResource
public interface StateTypeRepository extends JpaRepository<StormType,Long> {

}
